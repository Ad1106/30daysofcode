
class Calculator implements AdvancedArithmetic
{
 
@Override 
public int divisorSum(int n)
{
int sum = n;
for(int x=1;x<=n/2;x++)
{
 
if(n%x==0)
{
sum = sum + x;
}
 
}
return sum;
}
}

