// QQuicksort.cpp: 콘솔 응용 프로그램의 진입점을 정의합니다.
//

#include "stdafx.h"
#include <iostream>
using namespace std;


// 이 배열을,입력받은 배열로 대채 (배열의 포인터)

int start, end;

// 배열의 포인터와 배열 요소의 개수를 받는 함수

// int *list 부분 수정
void quicksort(int list[], int start, int end) { // 위에 선언된 배열을 포인터로 전달

	int pivot = start;
	int low = pivot + 1;
	int high = end;
	int tmp;

	if (start >= end) {
		return;
	} // 배열의 크기가 1이거나, start가 end보다 크면 return;으로 종료
	
	// else
	while (low <= end && list[pivot] >= list[low]) { // pivot보다 작은 원소가 제대로 있음을 확인 (정상 소팅)
		low++;
	} // 위의 조건일 동안 low 증가.
	while (high >= start && list[pivot] <= list[high]) { // pivot보다 큰 원소가 제대로 있음을 확인
		high++;
	}

	// 어떤 경우에 이렇게 바로 swap?
	if (low < high) {
		tmp = list[low];
		list[low] = list[high];
		list[high] = tmp;
	}
	// low > high 인경우,
	else {
		tmp = list[pivot];
		list[pivot] = list[high];
		list[high] = tmp;
	}

	// 분할된 리스트는?
	quicksort(list, start, high - 1);
	quicksort(list, high + 1, end);
	

}


int main(void)
{
	// (1) 배열 만들기 조건: 1<= n <=1000
	
	int list[1000];

	// (2) 배열의 입력 element 수 
	int size;
	scanf_s("%d", &size); // size가 포인터임. size의 주소값을 위해 &
	printf("배열의 요소를 입력해주세요\n");
	
	for (int j = 0; j < size; j++) {
		cin >> list[j]; // list가 포인터라서 앞에 &
		cout << endl;
	}
	// (4) 출력
	printf("출력시작");
	for (int i = 0; i < size; i++) {
		cout << list[i] << endl;
	}

	printf("quick sorting 중..\n");

	// (3) 퀵 정렬 
	quicksort(list, 0, size-1);

	// (4) 출력
	printf("출력시작");
	for (int i = 0; i < size; i++) {
		cout << list[i] << endl;
	}

    return 0;
}

