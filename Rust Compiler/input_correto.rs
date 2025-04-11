fn main() {
  let mut x: i32 = 10;
  let y = 20;
  let resultado: f64 = 0.0;

  if x > y {
      x = x + 1;
  } else {
      x = x - 1;
  }

  while x < 20 {
      x = x + 2;
  }

  for i in 0..10 {
      let temp = i * 2;
  }

  fn soma(a: i32, b: f64, c: i32) -> f64 {
      return a + b;
  }
}