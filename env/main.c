#include <stdlib.h>
#include<stdio.h>

void run();

int main() {
    printf("*-*---RUNNING 'flask run --reload --debugger' CMD---*-*");
    run();
    return 0;
}
void run(){
    system("flask run --reload --debugger");
}