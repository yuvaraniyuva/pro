#include<stdio.h>
#include<string.h>
int main()
{
	int num,i,j,arr[10000];
	int ele;
	scanf("%i%i",&num,&ele);
	for(i=0;i<num;i++)
	scanf("%d",&arr[i]);
	for(i=0;i<num-1;i++) 
{
for(j=i+1;j<num;j++)
{
if(ele==arr[i]+arr[j])
{
	printf("yes");
		return 0;
			}
		}
	}
printf("no");
return 0;
}
