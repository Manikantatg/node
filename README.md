step to do after the cloning<br>
pip install Flask networkx<br>
python app.py<br>
ctrl c to exit the task<br> 


#include<stdio.h>
#include<stdlib.h>
struct term
{
    int row;
    int col;
    int value;
};
struct term a[100],b[100];
void display(int value,struct term m[])
{
    int i;
    printf("rows\tcolumns\tvalues\n");
    for(i=0;i<=value;i++)
    {
        printf("%d\t%d\t%d\n",m[i].row,m[i].col,m[i].value);
    }
}
void create()
{
    int i, row,col,n;
    printf("Enter no. of rows, cols, values: ");
    scanf("%d%d%d",&row,&col,&n);
    a[0].row=row;
    a[0].col=col;
    a[0].value=n;
    for(i=1;i<=n;i++)
    {
        scanf("%d%d%d",&a[i].row,&a[i].col,&a[i].value);
    }
    display(n,a);
}
void transpose()
{
    int i,j,k=1,row,col,n;
    n=a[0].value;
    b[0].row=a[0].col;
    b[0].col=a[0].row;
    b[0].value=n;
    for(i=0;i<=a[0].col;i++)
    {
        for(j=1;j<=n;j++)
        {
            if(a[j].col==i)
            {
                b[k].row=a[j].col;
                b[k].col=a[j].row;
                b[k].value=a[j].value;
                k++;
            }
        }
    }
    display(n,b);
}
int main()
{
    int ch;
    while(1)
    {
        printf("\nMenu\n");
        printf("1.Create a sparse Matrix\n");
        printf("2.Transpose of a sparse Matrix\n");
        printf("3.exit\n");
        printf("Enter your choice: ");
        scanf("%d",&ch);

        switch (ch)
        {
        case 1:
            create();
            break;
        case 2:
            transpose();
            break;
        case 3:
            exit(0);
            break;
        default:
            printf("\nInvalid Option\n");
            break;
        }
    }
    return 0;
}
