public class ClassName
{
	// Attributes
	
	// x and y are between 0 and 10
	private int x, y;
	// s is not empty
	private String s;

	// Constructors
	public ClassName(int x, int y, String s)
	{
		setX(x);
		setY(y);
		setS(s);
	}

	// Methods
	public void setX(int x)
	{
		if(x < 0 || x > 10)
		{
			throw new IllegalArgumentException("x value is outside the range [0,10]");
		}
		this.x = x;
	}

	public int getX()
	{
		return x;
	}

	public void setY(int y)
	{
		if(y < 0 || y > 10)
		{
			throw new IllegalArgumentException("y value is outside the range [0,10]");
		}
		this.y = y;
	}

	public int getY()
	{
		return y;
	}

	private void setS(String s)
	{
		if(s.isEmpty())
		{
			throw new IllegalArgumentException("s string is empty");
		}
		this.s = s;
	}


	// Main
	public static void main(String [] args)
	{
		ClassName maClasse = new ClassName(1, 5, "maClasse"); // Correct
		ClassName maClasse2 = new ClassName(-1, 5, "maClasse2"); // throw an exception, x is negative
		ClassName maClasse3 = new ClassName(1, 5, ""); // throw an exception, s is empty
	}

}