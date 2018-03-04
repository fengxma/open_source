/**
 * This Triangle App takes a commandline arg specifying the number of 
 * rows to display for a Pascal's triangle.
 * Run "scala Triangle 5" in the commandline will give:
 * [
 *      [1],
 *     [1,1],
 *    [1,2,1],
 *   [1,3,3,1],
 *  [1,4,6,4,1]
 * ]
 */

import PascalTriangle.pascalTriangle
import PascalTriangle.pascalFancyDisplay

object Triangle {
  def main(args: Array[String]) {
    val ptri = pascalTriangle(args(0))
    pascalFancyDisplay(ptri)
  }
}