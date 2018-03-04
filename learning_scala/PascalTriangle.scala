/**
 * Given numRows, generate the first numRows of Pascal's triangle.
 * For example, given numRows = 5, show Pascal's Triangle like this:
 * [
 *      [1],
 *     [1,1],
 *    [1,2,1],
 *   [1,3,3,1],
 *  [1,4,6,4,1]
 * ]
 */

object PascalTriangle {
  def pascalTriangle (s: String): Array[Array[Int]] = {
    // require String s only contains positive digits (without minus sign)
    require(s forall Character.isDigit)
    // define rows as a Range traversable: [0,k)
    val rows = 0 until s.toInt  
    /**
     * define ptri as a 2-D array filled with 1s, e.g.:
     * [1]
     * [1,1]
     * [1,1,1]
     * [1,1,1,1]
     * [1,1,1,1,1]
     */
    val ptri = rows.toArray map (x => Array.fill(x+1)(1))
  
    /**
     * iterate through the 2-D array and calculate the value of 
     * each element based on the principle of Pascal's triangle
     */
    if (rows.length >= 2) {
      for {
        row <- ptri.indices.init
        if (row >= 1)
        col <- ptri(row).indices.init
      } {
        ptri(row+1)(col+1) = ptri(row)(col) + ptri(row)(col+1)
        }  
    }
    ptri
  }
    
  def pascalFancyDisplay (pascalTriangle: Array[Array[Int]]) {
    /**
     * Display Pascal's triangle in a pyramid shape. This method's
     * result type is Unit which can be omitted in the definition.
     * It's excuted for its side effects.
     */
    println("[")
    for {row <- pascalTriangle.indices} {
      if (row < pascalTriangle.indices.last)
        // mkString(start, sep, end)
        println(pascalTriangle(row).mkString(" "*(pascalTriangle.length-row)+"[", ",", "],"))
      else
        println(pascalTriangle(row).mkString(" "*(pascalTriangle.length-row)+"[", ",", "]"))
    }
    println("]")  
  }
}
