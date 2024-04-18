import java.util.Random;


/**
* A class for generating random bits.
*/

public class RandomBitGenerator 
{
    private static final int MAXSIZE = 128;
    public void generateRandomBits() 
    {
        Random random = new Random();
        for (int i = 0; i < MAXSIZE; i++)
            System.out.print(random.nextInt(2));
    }

    public static void main(String[] args) 
    {
        /* Creating a random bit generator object */    
        RandomBitGenerator generator = new RandomBitGenerator();
        generator.generateRandomBits();
    }
}