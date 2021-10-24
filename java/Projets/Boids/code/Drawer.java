import java.awt.EventQueue;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Polygon;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.RenderingHints;
import java.awt.Color;

public class Drawer extends JPanel 
{
    Polygon[] _polygons;
    Color[] _colors;
    int _nbDrawn = 0;

    public Drawer()
    {
        _polygons = new Polygon[500];
        _colors = new Color[500];
    }

    public void drawPolygon(int[] x, int [] y, int color)
    {
        if(_nbDrawn >= 500)
        {
            System.out.println("Error, the maximum number of polygons is reached");
            return;
        }
        if(_polygons[_nbDrawn] == null)
        {
            _polygons[_nbDrawn] = new Polygon(x, y, x.length);
        }
        else
        {
            _polygons[_nbDrawn].xpoints = x;
            _polygons[_nbDrawn].ypoints = y;
        }
        _colors[_nbDrawn] = new Color(color);
        _nbDrawn += 1;
    }

    private void doDrawing(Graphics g) 
    {
        RenderingHints rh = new RenderingHints(
                RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        rh.put(RenderingHints.KEY_RENDERING,
               RenderingHints.VALUE_RENDER_QUALITY);

        Graphics2D g2d = (Graphics2D) g;
        g2d.setRenderingHints(rh);

        for (int i = 0; i < _nbDrawn; i++) 
        {
            g2d.setPaint(_colors[i]);
            g2d.fillPolygon(_polygons[i]);
        }

        _nbDrawn = 0;
    }

    @Override
    public void paintComponent(Graphics g) 
    {
        super.paintComponent(g);
        doDrawing(g);
    }
}