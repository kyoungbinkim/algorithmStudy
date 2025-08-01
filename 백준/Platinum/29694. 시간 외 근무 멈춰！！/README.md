# [Platinum IV] 시간 외 근무 멈춰!! - 29694 

[문제 링크](https://www.acmicpc.net/problem/29694) 

### 성능 요약

메모리: 123120 KB, 시간: 408 ms

### 분류

많은 조건 분기, 그리디 알고리즘, 구현, 정렬

### 제출 일자

2025년 6월 18일 17:47:16

### 문제 설명

<p>올해 초 진행되던 개발 프로젝트가 끝나고 한숨 돌리던 말년 병장 준민이에게 새로운 개발 프로젝트가 들어왔다! 새로운 개발 프로젝트는 총 $N$개의 작업으로 이루어져 있다. $i$번째 작업을 완료하기 위해선 정확히 $t_i$회 근무를 진행해야 하며, 개발 프로젝트가 시작한 이후 $d_i$일이 지나기 전에 끝내야 한다. 그러나 평시 근무만으로는 모든 $N$개의 작업을 시간 내에 끝내기 힘들어 보였던 준민이는 개인 정비시간을 포기하며 시간 외 근무를 하고자 한다.</p>

<p>시간 외 근무를 평일에 하루 진행하면 가점 $A$점을 받을 수 있고, 주말에 하루 진행하면 가점 $B$점을 받을 수 있다. 주말에 시간 외 근무를 하는 것이 일반적으로 더 힘들기 때문에, 주말 시간 외 근무로 받는 가점은 평일 시간 외 근무로 받는 가점과 같거나 더 많다. 그러나, 앞으로 시간 외 근무로 받을 수 있는 가점은 최대 $M$점이라는 사실을 뒤늦게 깨달아 버린 준민이는 적당히 힘을 조절하여 정확히 가점 $M$점만 받도록 시간 외 근무를 하고자 한다.</p>

<p>개발 프로젝트는 월요일부터 시작하며, 평시 근무는 월요일부터 금요일까지만, 시간 외 근무는 요일과 관계없이 하루에 최대 한 번씩 진행할 수 있다. 근무마다 아직 완료되지 않은 작업을 선택하여 $1$회의 근무를 진행할 수 있으나, 준민이는 평시 근무 시간에는 일을 하는 척만 하며 근무하지 않을 수 있다. 다만, 시간 외 근무 시간에는 반드시 $1$회 근무를 진행한다고 한다.</p>

<p>또한, 주말만큼은 편안하게 생활관에서 쉬고 싶었던 준민이는 주말 시간 외 근무를 최소화하고자 한다. 이를 토대로 가점을 정확히 $M$점 얻으며 모든 작업을 마감 기한 이전에 끝낼 수 있는 최적의 근무표를 작성하던 준민이는 그만 잠에 빠져버리고 말았다! 깊게 잠이 든 준민이를 위해, 가점을 정확히 $M$점 얻으며 모든 작업을 마감 기한 이전에 끝낼 수 있는 주말 시간 외 근무의 최소 횟수를 구해주자.</p>

### 입력 

 <p>첫 번째 줄에 작업의 개수 $N$, 평일 시간외근무 가점 $A$, 주말 시간외근무 가점 $B$, 얻어야 하는 총 가점 $M$이 공백으로 구분되어 정수로 주어진다.</p>

<p>이후 $N$줄에 걸쳐 각 작업의 마감 기한을 나타내는 정수 $d_i$와 작업을 완료하는 데 필요한 근무 횟수를 나타내는 정수 $t_i$가 공백으로 구분되어 주어진다.</p>

### 출력 

 <p>가점을 정확히 $M$점 얻으며 모든 작업을 마감 기한 이전에 끝낼 수 있는 주말 시간 외 근무의 최소 횟수를 출력한다.</p>

<p>만약 어떻게 해도 가점을 정확히 $M$점 얻으며 모든 근무를 마감 기한 이전에 끝낼 수 없다면, <span style="color:#e74c3c;"><code>-1</code></span>을 출력한다.</p>

