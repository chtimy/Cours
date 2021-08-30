public class Epee
{
	// Attributs
	private  float attaque;
	public  float taille;
	public  String couleur;

	// Constructeur
	public Epee(float attaque, 
				float taille,
				String couleur)
	{
		setAttaque(attaque);
		this.taille = taille;
		this.couleur = couleur;
	}

	public float getAttaque()
	{
		return attaque;
	}

	private void setAttaque(float attaque)
	{
		if(attaque < 0)
		{
			throw new IllegalArgumentException("attaque est negatif");
		}
		this.attaque = attaque;
	}
}