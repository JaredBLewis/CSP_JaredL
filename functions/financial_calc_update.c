// Jared Lewis, Financial Calculator Update C
#include <stdio.h>
#include <math.h>
float income, rent, utilities, groceries, transportation, savings, spending;

void percent(char type[],int amount){
    int per = amount/ income *100;
    printf("The percent of your income for %s is %d%%.\n", type, per);
}

float user_input(char type[]){
    return (user_input("How much is your monthly %s?: ", type));

}

int main(void){
    // print statement that welcomes my user, and tells them what the program does.
    printf("\n");
    printf("Hi there! wlecome to my program!\n");
    printf("This program will calculate the best way to spend your money.\n");
    // ask what their income is (variable an input)
    income = user_input("income");
    // ask what their rent is (variable an input)
    printf("How much does your monthly rent cost?:");
    scanf("%d", &rent);

    // ask what their utilities is (variable an input)
    printf("How much does your monthly utilities cost?:");
    scanf("%d", &utilities);

    // ask what their groceries is (variable an input)
    printf("How much does your monthly groceries cost?:");
    scanf("%d", &groceries);

    // ask what their transportation is (variable an input)
    printf("How much does your monthly transportation cost?:");
    scanf("%d", &transportation);

    // calculate percent of income for each category
    float savings = income * 0.1;
    float spending = (float)income - savings - rent - utilities - groceries - transportation;
    float per_rent = (float)rent / income * 100;
    float per_utilities = (float)utilities / income * 100;
    float per_groceries = (float)groceries / income * 100;
    float per_transportation = (float)transportation / income * 100;
    float per_spending = (float)spending / income * 100;

    // give
    percent("rent", rent);
    percent("uttilities", utilities);
    percent("groceries", groceries);
    percent("transportation", transportation);
    percent("savings", savings);
    percent("spending", spending);
    return 0;
}