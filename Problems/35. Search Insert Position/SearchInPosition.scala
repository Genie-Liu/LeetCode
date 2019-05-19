object Solution {
  def searchInsert(nums: Array[Int], target: Int): Int = {
    if (target <= nums(0)) 0
    else if (target == nums(nums.length - 1)) nums.length - 1
    else if (target > nums(nums.length - 1)) nums.length
    else
      _search_helper(nums, target, 0, nums.length - 1)
  }

  def _search_helper(nums: Array[Int], target: Int, low: Int, high: Int): Int = {
    if (low + 1 == high)
      low + 1
    else {
      val middle = (low + high) / 2
      if (target == nums(middle))
        middle
      else if (target < nums(middle))
        _search_helper(nums, target, low, middle)
      else
        _search_helper(nums, target, middle, high)
    }
  }
}