// Jared Lewis, My Family Loop C
#include <stdio.h>

char siblings [10][20] = {
    "Ty", 
    "Kaden", 
    "Nephi", 
    "Abish", 
    "Jared", 
    "Daniel", 
    "Nathan", 
    "Noah", 
    "Elijah", 
    "Pearl"
};
int i;

int main(void){
    for(i=0; i<10; i++){
        printf("Hello %s!\n", siblings[i]);
    }
    return 0;
}