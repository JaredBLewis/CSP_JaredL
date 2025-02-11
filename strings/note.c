// Jared Lewis, Strings Notes C
#include <stdio.h>
char subject[50];
char name[] = "Victoria";
char sentence[] = "The quick brown fox jumps over the lazy dog.";

int main(void){
    //printf("What class are you in?:\n");
    //scanf("%s", subject);
    //fgets(subject, sizeof(subject), stdin);
    //printf("You are in %s, that is a cool class!", subject);
    //name[0] = 'T';
    //name[1] = 'o';
    //name[2] = 'r';
    //name[3] = 'i';
    //name[4] = ' ';
    //name[5] = ' ';
    //name[6] = ' ';
    //name[7] = ' ';
    //prinf("%s", name);
    //printf("%lu\n",sizeof(sentence));
    //printf("%d\n",strlen(sentence));
    char one[] = "Hello ";
    char two[] = "World!";
    char three[] = "Welcome to my program. ";
    printf("%s\n", one);
    strcat(one, two);
    printf("%s\n", one);
    strcat(three, one);//can only cncatenate 2 things at a time.
    printf("%s\n", three);
    return 0;
}