<a id="readme-top"></a>
<div align="center">
  <a href="#readme-top">
    <img alt="Assignment: JavaScript — Warm up" src="https://img.shields.io/badge/Assignment-JavaScript%20--%20Warm%20up-blue">
  </a>
  <a href="#task-list">
    <img alt="Tasks: 18" src="https://img.shields.io/badge/Tasks-18-6c757d">
  </a>
</div>

---

# JavaScript — Warm up

This project is a first walk through JavaScript with Node.js in the terminal.  
You print messages, read arguments, loop, write small functions, and touch objects and modules.

---

## How I check my files
- `semistandard *.js` → check style.
- `wc -l file.js` → count total lines.
- `wc -L file.js` → check the longest line.

---

<a id="task-list"></a>

## 0) First constant, first print — `0-javascript_is_amazing.js`
- **What it does:** Prints the sentence `JavaScript is amazing` using a constant.
- **Key idea:** Use `const` and `console.log` to show a simple message.
- **In short:** One constant, one print, one line of output.

---

## 1) 3 languages — `1-multi_languages.js`
- **What it does:** Prints three lines: `C is fun`, `Python is cool`, `JavaScript is amazing`.
- **Key idea:** Call `console.log` several times in a row.
- **In short:** Three short messages, one after another.

---

## 2) Arguments — `2-arguments.js`
- **What it does:** Looks at how many arguments you passed to the script.
- **Key idea:** Use `process.argv` to count extra values after the script name.
- **In short:** Says if there are no arguments, one argument, or many arguments.

---

## 3) Value of my argument — `3-value_argument.js`
- **What it does:** Prints the first argument passed to the script.
- **Key idea:** Read `process.argv[2]` and check if it exists.
- **In short:** Shows the first extra word you give, or says `No argument`.

---

## 4) Create a sentence — `4-concat.js`
- **What it does:** Prints `<firstArg> is <secondArg>`.
- **Key idea:** Join two arguments with the word `is` in the middle.
- **In short:** Builds a tiny sentence from what you type.

---

## 5) An Integer — `5-to_integer.js`
- **What it does:** Tries to turn the first argument into an integer and prints it.
- **Key idea:** Use `parseInt` and `isNaN` to decide if it is a number.
- **In short:** Says `My number: n` or `Not a number`.

---

## 6) Loop to languages — `6-multi_languages_loop.js`
- **What it does:** Stores three strings in an array and prints them in a loop.
- **Key idea:** Use a `for` loop to walk through an array.
- **In short:** Same three lines as before, but now driven by a loop.

---

## 7) I love C — `7-multi_c.js`
- **What it does:** Prints `C is fun` a certain number of times.
- **Key idea:** Turn the first argument into a number and loop that many times.
- **In short:** Repeats the same line x times, or says the count is missing.

---

## 8) Square — `8-square.js`
- **What it does:** Prints a square made of `X` characters.
- **Key idea:** Use a loop and `repeat` to draw rows based on the size argument.
- **In short:** Draws an `X` box when the size is a positive number.

---

## 9) Add — `9-add.js`
- **What it does:** Reads two arguments, converts them, and prints their sum.
- **Key idea:** Wrap the addition in a small `add(a, b)` function.
- **In short:** A tiny calculator that only does `a + b`.

---

## 10) Factorial — `10-factorial.js`
- **What it does:** Computes the factorial of the first argument and prints it.
- **Key idea:** Use a recursive function that calls itself until it reaches 1.
- **In short:** Multiplies all numbers down to 1, or prints 1 when missing.

---

## 11) Second biggest! — `11-second_biggest.js`
- **What it does:** Finds the second biggest integer among the arguments.
- **Key idea:** Convert all arguments to numbers, sort them, and pick the second one.
- **In short:** Gives you the “runner-up” number, or 0 if there are not enough.

---

## 12) Object — `12-object.js`
- **What it does:** Logs an object, changes its `value` from 12 to 89, then logs it again.
- **Key idea:** Show that object properties can be updated after creation.
- **In short:** Same object, new `value`, printed twice.

---

## 13) Add file — `13-add.js`
- **What it does:** Exports an `add(a, b)` function for other files to use.
- **Key idea:** Use `module.exports` so `require('./13-add').add` works.
- **In short:** A shared helper that returns the sum of two numbers.

---

## 14) Const or not const — `100-let_me_const.js`
- **What it does:** Changes the global variable `myVar` to 333 when this file runs.
- **Key idea:** Show how requiring a file can change a variable defined outside.
- **In short:** You set `myVar = 89`, require this file, and then `myVar` becomes 333.

---

## 15) Call me Moby — `101-call_me_moby.js`
- **What it does:** Calls a given function `x` times.
- **Key idea:** Take a callback and a count, and loop to call the callback again and again.
- **In short:** A helper that repeats some action many times for you.

---

## 16) Add me maybe — `102-add_me_maybe.js`
- **What it does:** Increments a number and then calls a function with the new value.
- **Key idea:** Change the number first, then pass it into the callback.
- **In short:** “Take this number, add one, and give it to my function.”

---

## 17) Increment object — `103-object_fct.js`
- **What it does:** Adds an `incr` function to an object that increases its `value`.
- **Key idea:** Attach a method to an object and use `this` to update a property.
- **In short:** An object that can bump its own number each time you call `incr()`.
