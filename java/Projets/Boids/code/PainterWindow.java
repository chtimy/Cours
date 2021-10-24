import javax.swing.JFrame;

public class PainterWindow extends JFrame 
{
    public PainterWindow(Drawer drawer, int width, int height, String title) 
    {
        add(drawer);
        setTitle(title);
        setSize(width, height);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}