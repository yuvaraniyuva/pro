#include <stdio.h>
int main()
{
	int num,a[100],i,j,c[100],ca=0;
  scanf("%d",&num);
	c[0]=0;
	for(i=0;i<num;i++)
	{
	scanf("%d",&a[i]);
	c[i]=1;
	}
	for(i=1;i<num;i++)
	{
	 if(a[i]>a[i-1])
	 c[i]=c[i-1]+1;
	}
	for(i=0;i<num;i++)
	ca+=c[i];
	printf("%d",ca);
	return 0;
}
