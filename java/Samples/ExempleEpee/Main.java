class Main
{
	public static void main(String[] args)
	{
		Epee monEpee = new Epee(20, 1, "gris");
		Epee monEpee2 = new Epee(10, 0.5f, "blanc");

		System.out.println("monEpee : " + monEpee.getAttaque() + "," + monEpee.taille + "," + monEpee.couleur);
		System.out.println("monEpee2 : " + monEpee2.getAttaque() + "," + monEpee2.taille + "," + monEpee2.couleur);

		float monAttaque = monEpee.getAttaque();
		monAttaque = -5;

		monEpee.setAttaque(-5);

		System.out.println("monEpee : " + monEpee.getAttaque() + "," + monEpee.taille + "," + monEpee.couleur);

	}
}