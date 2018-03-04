/*
 * This script solves a specific ordering problem
 * as follows: put the last element of a list behind
 * the first, the second to the last behind the second, etc.
 * For example, a list (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) should
 * be reordered into (1, 10, 2, 9, 3, 8, 4, 7, 5, 6).
 * This algorithm has a time complexity of O(n^2) 
 */
/*
 * According to scala List's basic structure,
 * a new element (single-member list) can only
 * be prepended to the beginning of the list.
 * Therefore, in y :: ys, y is an element while
 * ys can be element(s) of list.
 * Double colons (::) means "construct", 
 * pronounced as "cons".
 */

/*
 * Despite its brevity, this recursive function is not space/memory efficient.
 * Each recursive call creates a new val(?) requiring a new stack frame.
 * (note: parameter decaration is implicitly prefixed with val)
 * It cannot be applied to lists of much more than ca. 30,000 to 50,000 elements.
 * The recursive call here is not tail recursive as reorder occurs inside
 * a :: operation (which is right associative). A tail recursive implementation
 * would be optimized by Scala compiler and thus become more efficient.
 */

def reorder (xs: List[Int]): List[Int] = xs match {  
  case List() => List() // empty list doesn't need reordering
  case y :: Nil => xs // list(a) doesn't need reordering
  case y :: y1 :: Nil => xs // list(a, b) doesn't need reordering
  case y :: ys => y :: ys.last :: reorder(ys.init) // recursion
  // ys.init traverse the list to get all elements before the last (non-Nil),
  // so it takes more time as a list gets longer.
}

// Initialize alist with values as (1, 2, 3, 4, 5, 6, 7, 8, 9)
val alist = List.range(1, 10)
//val alist = List.tabulate(1000)(n => n+1)
val reordered = reorder(alist)
println(reordered.mkString("", " ", ""))
// Output should be: 1 9 2 8 3 7 4 6 5