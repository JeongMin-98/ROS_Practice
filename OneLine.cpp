#include <iostream>
#include <fstream>
#include "opencv2/opencv.hpp"

// declare
std::pair<int, int> process_image(cv::Mat& src);
void draw_lines(cv::Mat& img, std::vector<cv::Vec4i> line);
void draw_lines(cv::Mat& src, float m, float b, bool left, bool right);
void color_filter_hsv(cv::Mat& src, cv::Mat& dst);
void color_filter_hls(cv::Mat& src, cv::Mat& dst);
void draw_rectangle(cv::Mat& src, int& lpos, int& rpos);
std::pair<std::vector<cv::Vec4i>, std::vector<cv::Vec4i>>divide_left_right(std::vector<cv::Vec4i>& lines);
std::pair<float, float> get_line_params(std::vector<cv::Vec4i>& lines);
std::pair<int, std::pair<float, float>> get_line_pos(std::vector<cv::Vec4i>& lines, bool left, bool right);

// 전역 변수 선언
int OFFSET = 335;
float RATIO = 1.5f;
int GAP = 40;
int WIDTH = 640;
int HEIGHT = 480;
bool leftDetector = true;
bool rightDetector = true;
float error;

int main()
{
	// 비디오 cap 열기
	cv::VideoCapture cap("Sub_project.avi");
	// FPS 설정
	cap.set(cv::CAP_PROP_FPS, 15);

	if (!cap.isOpened()) {
		std::cerr << "load failed!" << std::endl;
		return -1;
	}

	cv::Mat src;
	std::pair<int, int> lposAndRpos;
	// 영상 딜레이 설정
	int delay = cvRound(1000 / 30);
	int idx = 0;
	int frame = 0;
	float lpos;
	float rpos;
	// lpos, rpos 결과 작성을 위한 파일 스트림 객체 생성
	//std::ofstream fout;
	// fout.open("result.csv", std::ofstream::trunc);
	//fout << "Index,frame,lpos,rpos" << std::endl;
	while (true)
	{
		
		cap >> src;

		if (src.empty()) {
			std::cerr << "Empty frame!" << std::endl;
			break;
		}

		lposAndRpos = process_image(src);
		lpos = lposAndRpos.first;
		rpos = lposAndRpos.second;
		cv::imshow("result", src);


		if (!leftDetector || !rightDetector)
		{
			std::cout << "idx: " << idx << "frame: " << frame << "left:" << lpos << "right : " << rpos << std::endl;
			std::cout << "error : " << error << std::endl;
			std::cout << "leftOnly : " << leftDetector << std::endl;
			std::cout << "rightOnly : " << rightDetector << std::endl;
		}
			
		if (frame % 60 == 0) {
			// 출력부
			
			// fout << idx << "," << frame << "," << lpos << "," << rpos << std::endl;
			//++idx;
			/**
			std::string filename = "D:/\image/\lane";
			filename += std::to_string(frame);
			filename += ".bmp";
			std::cout << filename;
			cv::imwrite(filename, src);
			*/
			
			
		}
		++idx;
		++frame;
		

		if (cv::waitKey(delay) == 27) {
			break;
		}

	}
	// fout.close();
	return 0;
}

// image process
std::pair<int, int> process_image(cv::Mat& src)
{

	// declare line value
	std::pair<std::vector<cv::Vec4i>, std::vector<cv::Vec4i>> leftRightLinesPair;
	std::vector<cv::Vec4i> leftLines, rightLines;
	// declare position and slope vlaues
	std::pair<int, std::pair<float, float>> tempPosSlope;
	int lpos, rpos;
	float leftSlope, rightSlope, leftB, rightB;
	
	// color_filter
	cv::Mat filtered_img;
	color_filter_hsv(src, filtered_img);
	// color_filter_hls(src, filtered_img);
	// cv::imshow("hsv", filtered_img);
	
	// 그레이스케일 색변환
	cv::Mat gray;
	cvtColor(src, gray, cv::COLOR_BGR2GRAY);
	// 가우시안 블러 처리
	cv::Mat blur;
	cv::GaussianBlur(gray, blur, cv::Size(), 1.);
	// cv::imshow("blur", blur);
	
	// avg_kernel 평균 필터 적용
	// cv::Mat avg_kernel = cv::Mat::ones(5, 5, CV_32F) / 25;
	// filter2D(filtered_img, blur, -1, avg_kernel, cv::Point(-1, -1), (0, 0), 4);
		
	// canny 처리
	cv::Mat canny;
	//	cv::Canny(blur, canny, 60, 70);
	cv::Canny(blur, canny, 150, 200);
	// cv::imshow("Canny", canny);
	cv::Mat roi;

	roi = canny(cv::Rect(0, OFFSET, WIDTH, GAP));
	
	// roi houghlineP
	std::vector<cv::Vec4i> allLines;
	cv::HoughLinesP(roi, allLines, 1, CV_PI / 180, 20, 15, 7);
	
	// line is empty  
	if (allLines.size() == 0)
		return std::pair<int, int>(0, 0);
	
	// divide left and right_lines;
	leftRightLinesPair = divide_left_right(allLines);
	leftLines = leftRightLinesPair.first;
	rightLines = leftRightLinesPair.second;

	// Draw lines
	draw_lines(src, leftLines);
	draw_lines(src, rightLines);
	
	// get position and slope values from left_pos
	tempPosSlope = get_line_pos(leftLines, true, false);
	lpos = tempPosSlope.first;
	leftSlope = tempPosSlope.second.first;
	leftB = tempPosSlope.second.second;

	// get position and slope values from right_pos
	tempPosSlope = get_line_pos(rightLines, false, true);
	rpos = tempPosSlope.first;
	rightSlope = tempPosSlope.second.first;
	rightB = tempPosSlope.second.second;


	int estimatedMidX = lpos + rpos;
	error = (static_cast<float>(estimatedMidX) - 640.0) / 640.0f;

	if (error > 0.2)
	{
		leftDetector = true;
		rightDetector = false;
	}
	else if (error < - 0.2)
	{
		leftDetector = false;
		rightDetector = true;
	}
	else if (abs(error) <= 0.2)
	{
		leftDetector = true;
		rightDetector = true;
	}


	// draw_lines(src, leftSlope, leftB, true, false);
	// draw_lines(src, rightSlope, rightB, false, true);


	return std::pair<int, int>(lpos, rpos);

}

// draw lines on src image
void draw_lines(cv::Mat& src, std::vector<cv::Vec4i> line)
{
	cv::Point2i pt1, pt2;
	for (auto& draw : line)
	{
		// x1 draw[0]
		// y1 draw[1]
		// x2 draw[2]
		// y2 draw[3]

		/**
			y = mx + b

			y = 0 , x = -b/m
			y = 400 x = (400 - b) / m + 320 => right

		

		**/
		pt1 = cv::Point2i(draw[0], draw[1] + OFFSET);
		pt2 = cv::Point2i(draw[2], draw[3] + OFFSET);

		cv::line(src, pt1, pt2, (0, 0, 255), 2);
	}
}

void draw_lines(cv::Mat& src, float m, float b, bool left, bool right)
{
	cv::Point2i pt1, pt2;

	if ((m == 0.0) && (b == 0.0))
		return;
	if (left == true)
	{
		pt1.x = static_cast<int>(-b / m);
		pt1.y = GAP;
		pt2.x = static_cast<int>((480.0 - b) / m);
		pt2.y = 400;
	}
	else
	{
		pt1.x = static_cast<int>(-b / m);
		pt1.y = GAP;
		pt2.x = static_cast<int>((480.0 - b) / m);
		pt2.y = 480;
	}

	cv::line(src, pt1, pt2, (0, 255, 0), 2);
}

// draw rectanges roi
void draw_rectangle(cv::Mat& src, int& lpos, int& rpos)
{
	cv::rectangle(src, cv::Point(lpos - 5, 400 - 10), cv::Point(lpos + 5, 400 + 10), (0, 255, 0), 1);
	cv::rectangle(src, cv::Point(rpos - 5, 400 - 10), cv::Point(rpos + 5, 400 + 10), (0, 255, 0), 1);
}


// divide the lines left and right
std::pair<std::vector<cv::Vec4i>, std::vector<cv::Vec4i>> divide_left_right(std::vector<cv::Vec4i>& lines)
{
	std::pair<std::vector<cv::Vec4i>, std::vector<cv::Vec4i>> leftRightLinesPair;
	std::vector<cv::Vec4i> newLines;
	std::vector<float> slopes;
	cv::Vec4i line;


	float slope_range = 10.0;

	int x1, y1, x2, y2;
	float slope;

	for (int i = 0; i < lines.size(); ++i)
	{
		line = lines[i];
		x1 = line[0], y1 = line[1];
		x2 = line[2], y2 = line[3];
		if (x2 - x1 == 0)
		{
			slope = 0.0;
		}
		else {
			slope = static_cast<float>(y2 - y1) / static_cast<float>(x2 - x1);
		}
// Set slope ranges
# if 0
		if (std::abs(slope) <= slope_range)
		{
			slopes.push_back(slope);
			new_lines.push_back(line);
		}
# else
		if (std::abs(slope) > 0 && std::abs(slope) <= 10)
		{
			slopes.push_back(slope);
			newLines.push_back(line);
		}
# endif
	}

	// declare values
	std::vector<cv::Vec4i> tempLeftLines, tempRightLines, Final_left_line, Final_right_line;
	std::vector<float> leftLinesSlope, rightLinesSlope;

	// divide lines right and left
	for (int i = 0; i < newLines.size(); ++i)
	{
		line = newLines[i];
		slope = slopes[i];

		x1 = line[0], y1 = line[1];
		x2 = line[2], y2 = line[3];
#if 0            
		if ((slope < 0) && (x2 < center))
			leftLineIndices.push_back(i);
		else if ((slope > 0) && (x1 > center))
			rightLineIndices.push_back(i);
#else
		if (leftDetector && rightDetector)
		{
			if ((slope < 0) && (x2 < 320))
				Final_left_line.push_back(line);
			else if ((slope > 0) && (x1 > 320))
				Final_right_line.push_back(line);
		}
		else if (!leftDetector && rightDetector)
		{
			if (slope > 0)
				Final_right_line.push_back(line);
		}
		else if (leftDetector && rightDetector)
		{
			if (slope < 0)
				Final_left_line.push_back(line);
		}
#endif
	}
	
	leftRightLinesPair = std::make_pair(Final_left_line, Final_right_line);
	return leftRightLinesPair;
}

// Get line params
std::pair<float, float> get_line_params(std::vector<cv::Vec4i>& lines)
{
	int size = lines.size();
	if (lines.empty())
		return std::pair<float, float>(0.0f, 0.0f);

	int x1, y1, x2, y2;
	float x_sum = 0.0, y_sum = 0.0, m_sum = 0.0;
	float x_avg, y_avg, m, b;


	// line 별로 m, y, b의 합 구하기
	for (auto& line : lines)
	{
		x1 = line[0], y1 = line[1];
		x2 = line[2], y2 = line[3];

		x_sum += x1 + x2;
		y_sum += y1 + y2;

		m_sum += static_cast<float>(y2 - y1) / static_cast<float>(x2 - x1);
	}

	x_avg = x_sum / static_cast<float>(size * 2);
	y_avg = y_sum / static_cast<float>(size * 2);

	// 최종 m,b 구하기
	m = m_sum / static_cast<float>(size);
	b = y_avg - m * x_avg;


	return std::pair<float, float>(m, b);
}

// Get line pos
std::pair<int, std::pair<float, float>> get_line_pos(std::vector<cv::Vec4i>& lines, bool left, bool right)
{
	float width = 640.0;
	std::pair<float, float> params = get_line_params(lines);
	float m = params.first;
	float b = params.second;
	float y, pos;

	if (m == 0.0 && b == 0.0)
	{
		if (left == true)
		{
			pos = 0.0;
		}
		else
		{
			pos = width;
		}
	}
	else
	{
		// roi의 height: Gap
		// offset: 340
		// offset => src 영상의 y축 시작 점
		// 최종 결과인 y축이 400일때 좌표를 구하기 위해서 다음과 같은 y좌표를 계산
		// Offset + y => 400이 되도록 설정
		// Offset + Gap * ratio = 400
		// 340 + 40 * 1.5 = 400
		y = GAP * RATIO;
		pos = (y - b) / m;
	}
	return { static_cast<int>(pos), params };
}


// hsv색공간에서 검정색 색 추출
void color_filter_hsv(cv::Mat& src, cv::Mat& dst)
{
	cv::Mat mask;
	cv::Mat hsv;
	cv::Mat res;

	cv::cvtColor(src, hsv, cv::COLOR_BGR2HSV);
	cv::Scalar lower(0, 0, 180);
	cv::Scalar upper(255, 111, 255);

	cv::inRange(hsv, lower, upper, mask);
	cv::bitwise_and(src, src, res, mask);

	cv::cvtColor(res, dst, cv::COLOR_HSV2BGR);
	cv::cvtColor(dst, dst, cv::COLOR_BGR2GRAY);

}


// hls색공간에서 검정색 추출
void color_filter_hls(cv::Mat& src, cv::Mat& dst)
{
	cv::Mat mask;
	cv::Mat hsl;


	cv::cvtColor(src, hsl, cv::COLOR_BGR2HLS);
	cv::Scalar lower(0, 0, 0);
	cv::Scalar upper(255, 255, 15);
	cv::inRange(hsl, lower, upper, mask);

	dst = mask;

}