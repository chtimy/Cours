public class Demo
{
    public static void main(String[] args) 
    {
        // Creation d'un nouveau pinceau
        Drawer drawer = new Drawer();
        // Creation d'une surface pour dessiner
        PainterWindow window = new PainterWindow(drawer, 1024, 768, "Boids simulation");
        // Rendre la surface visible
        window.setVisible(true);

        float i = 0;
        // Boucle de mise à jour des dessins
        while(true)
        {
            // Dessine deux triangles de couleur différentes. La coordonnées x du premier sommet
            // de chaque triangle avance de 0.5 pixel tous les 1/60 de secondes
            drawer.drawPolygon(new int[]{100+(int)i, 100, 200}, new int[]{100, 200, 100}, 0xff0000);
            drawer.drawPolygon(new int[]{300+(int)i, 300, 400}, new int[]{300, 400, 300}, 0x00ff00);
            // Efface le dessin et redessine les nouvelles instructions ci-dessus => drawPolygon
            drawer.repaint();
            i+=0.5;

            // Ce bloc permet de faire dormir la boucle pendant 1/60 secondes
            try {
                 Thread.sleep(1000/60);
            } catch (InterruptedException e) 
            {
                System.out.println(e);
            }
        }
    }
}