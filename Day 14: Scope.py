
    public Difference(int []arr)
 {
     
     this.elements = arr;
 }
public void computeDifference()
{
    bubbleSort(elements);
    
    maximumDifference=Math.abs(elements[0]- elements[(elements.length-1)]);
    
}
 
    public static void bubbleSort(int arr[])
 
    {
        int temp;
 
        for(int x=0; x<arr.length-1;x++) 
        { 
            for(int y=0;y<arr.length-x-1;y++) 
            {
                if(arr[y]>arr[y+1])
                {
                    temp=arr[y];
                    arr[y]=arr[y+1];
                    arr[y+1]=temp;
                }
            }
                
        }
    }
