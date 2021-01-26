// 99 bottles of beer exercise

public class helloworld{
    public static void main(String[] args){
        int bottleCount = 99;
        while(bottleCount > 0){
            System.out.println(bottleCount + " bottles of beer on the wall, " + bottleCount + " bottles of beer.");
            bottleCount = bottleCount - 1;
            System.out.println("Take one down, pass it around, " + bottleCount + " bottles of beer on the wall...");
        }
        if(bottleCount==0){
            System.out.println("No more bottles of beer on the wall, no more bottles of beer.");
            System.out.println("Go to the store and buy some more, 99 bottles of beer on the wall...");
        }

        // Random numbers
    
        System.out.println((int) (Math.random()*10));
    }
}