public class Demo
{
    public static void main(String[] args) 
    {
        Drawer drawer = new Drawer();
        PainterWindow window = new PainterWindow(drawer, 1024, 768, "Boids simulation");
        window.setVisible(true);

        float i = 0;
        while(true)
        {
            drawer.drawPolygon(new int[]{100+(int)i, 100, 200}, new int[]{100, 200, 100}, 0xff0000);
            drawer.drawPolygon(new int[]{300+(int)i, 300, 400}, new int[]{300, 400, 300}, 0x00ff00);
            drawer.repaint();

            try {
                 Thread.sleep(1000/60);
            } catch (InterruptedException e) 
            {
                System.out.println(e);
            }

            i+=0.5;
        }
    }
}