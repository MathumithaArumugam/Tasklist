import java.lang.Math;
class Point
{
    int xCoordinate,yCoordinate;
    Point(int x,int y)
    {
        this.xCoordinate=x;
        this.yCoordinate=y;
    }
    public static double getEuclideanDistance(Point p1,Point p2)
    {
        int sum=(p2.xCoordinate-p1.xCoordinate)*(p2.xCoordinate-p1.xCoordinate)+(p2.yCoordinate-p1.yCoordinate)*(p2.yCoordinate-p1.yCoordinate);
        return(Math.sqrt(sum));
    }
}