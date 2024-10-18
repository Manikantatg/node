step to do after the cloning<br>
pip install Flask networkx<br>
python app.py<br>
ctrl c to exit the task<br> 


#include<stdlib.h>
#include<stdio.h>
#define MAX 6
int stack[MAX],ele,num,top=-1;
void push(int);
int pop();
void stakstatus();
void display();
int main()
{
 int ch;
while(1)
{
printf("\n1.push \n2.pop \n3.stack status \n4.display\n5.Exit\n Enter your choice:");
scanf("%d",&ch);
switch(ch)
{
case 1:
printf("\n Enter element to push: ");
scanf("%d", &ele);
push(ele);
break;
case 2:
ele = pop();
printf("\n popped element from stack: %d",ele);
break;
case 3:
stakstatus();
break;
case 4:
display();
break;
case 5:
exit(0);
}
}
}
void push(int ele)
{
if (top ==MAX - 1)// if top==max-1 stack is full...
{
printf("\n stack is overflow...\n"); 
}
else{
stack[++top]= ele;//increment top and push element to stack
}
}
int pop()
{
if (top ==-1)//if top=-1 stack is empty you cannot pop element
{
 printf("\n stack is underflow! \n");
 }
else
{
return stack[top--];//pop last element inserted from stack
}
}
void stakstatus()
{
if(top == MAX -1)//check the condition to stack full or not 
{
printf("stack is full");
}
 display();
}
void display()
{
 int i;
if (top ==-1)
{
printf("stack is empty!\n");
}
else
{
printf("stack else are \n");
for (i=top;i>=0;i--)
{
printf("%d\n",stack[i]);
}
}
}
