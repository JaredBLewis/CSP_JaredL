// Jared Lewis, Hello World Update C
#include <stdio.h>

void greeting(char name[]){
    return (printf("Hello, %s!\n", name));
}

int main(void){
    greeting("Jared");
    greeting("Jack");
    greeting("Bob");
    greeting("Alice");
    greeting("Yenesis");
    return 0;
}