let a = Number(prompt('Введите целое число от 0 до 9:'));
switch (a) {
  case 0:
    console.log('ноль');
    break;
  case 1:
    console.log('один');
    break;
  case 2:
    console.log('два');
    break;
  case 3:
    console.log('три');
    break;
  case 4:
    console.log('четыре');
    break;
  case 5:
    console.log('пять');
    break;
  case 6:
    console.log('шесть');
    break;
  case 7:
    console.log('семь');
    break;
  case 8:
    console.log('восемь');
    break;
  case 9:
    console.log('девять');
    break;
  default:
    console.log('Введи верные условия');
    break;
}

//====================================================================================================

var nums = [4, 3, 2, 7, 11, 15];
var target = 9;
var twoSum = function (nums, target) {
  // Массив для хранения результата
  result = [];
  //хранение результата
  index_map = new Map();
  // Цикл для каждого элемента в массиве
  for (let i = 0; i < nums.length; i++) {
    let difference = target - nums[i];
    if (index_map.has(difference)) {
      result[0] = i;
      result[1] = index_map.get(difference);
      break;
    } else {
      index_map.set(nums[i], i);
    }
  }
  return result;
};

console.log(twoSum(nums, target));
