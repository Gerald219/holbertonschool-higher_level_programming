# JavaScript - Warm up

This folder contains small Node.js scripts to warm up with JavaScript on the command line:
printing text, working with arguments, loops, functions, objects, and modules.

## Environment and rules

- All scripts run on **Ubuntu 20.04 LTS** with **Node.js 14.x**
- First line of every file: \`#!/usr/bin/node\`
- Code is **semistandard** compliant (Standard + semicolons) except where the project says otherwise
- No use of \`var\`, only \`const\` and \`let\`
- Every file must be executable (\`chmod +x file.js\`)

To run a script:

\`\`\bash
./file.js            # when executable bit is set
# or
node file.js
\`\`\

To lint with semistandard:

\`\`\bash
semistandard *.js
\`\`\

> Note: \`100-let_me_const.js\` is allowed to fail semistandard per the project instructions.

---

## Task list

### 0. First constant, first print — \`0-javascript_is_amazing.js\`

- Creates a constant \`myVar\` with the text **"JavaScript is amazing"**
- Prints it with \`console.log\`

### 1. 3 languages — \`1-multi_languages.js\`

- Prints three lines one after another:
  - \`C is fun\`
  - \`Python is cool\`
  - \`JavaScript is amazing\`

### 2. Arguments — \`2-arguments.js\`

- Looks at how many command line arguments are passed (after the script name)
- Prints:
  - \`No argument\` if there are none
  - \`Argument found\` if there is exactly one
  - \`Arguments found\` if there are two or more

### 3. Value of my argument — \`3-value_argument.js\`

- Prints the **first** argument only
- If there is no argument, prints \`No argument\`

### 4. Create a sentence — \`4-concat.js\`

- Takes two arguments and prints:  
  - \`firstArg is secondArg\`
- If one or both arguments are missing, the word \`undefined\` appears in their place (as in the examples)

### 5. An Integer — \`5-to_integer.js\`

- Takes the first argument and tries to convert it to an integer with \`parseInt\`
- If it is not a number, prints \`Not a number\`
- Otherwise prints \`My number: <integer>\`

### 6. Loop to languages — \`6-multi_languages_loop.js\`

- Stores the three text lines in an array
- Uses a **loop** to go through the array and print each line with \`console.log\`

### 7. I love C — \`7-multi_c.js\`

- First argument is a number \`x\`
- If \`x\` is not a number, prints \`Missing number of occurrences\`
- Otherwise prints \`C is fun\` exactly \`x\` times in a loop

### 8. Square — \`8-square.js\`

- First argument is the size of a square
- If it is not a number, prints \`Missing size\`
- If it is a positive number, prints a square made of \`X\` with that size (width and height)
- Negative values result in no output, matching the example

### 9. Add — \`9-add.js\`

- Defines a function \`add(a, b)\` that returns the sum of two numbers
- Reads two arguments from the command line, converts them to integers, and prints \`add(a, b)\`

### 10. Factorial — \`10-factorial.js\`

- Defines a recursive function to compute factorial
- Uses the first argument as the number
- If the argument is missing or not a number, the factorial is treated as 1
- Prints the factorial result (which can be very large)

### 11. Second biggest! — \`11-second_biggest.js\`

- Reads all integer arguments from the command line
- If there are fewer than two numbers, prints \`0\`
- Otherwise finds and prints the **second biggest** number

### 12. Object — \`12-object.js\`

- Creates an object with a \`value\` field set to 12 and prints it
- Changes \`value\` to 89 and prints the same object again to show the update

### 13. Add file — \`13-add.js\`

- Exports a function \`add(a, b)\` so another file can do:
  - \`const add = require('./13-add').add;\`
- Calling \`add(3, 5)\` returns 8

---

## Advanced tasks

### 14. Const or not const — \`100-let_me_const.js\`

- Changes the value of a global variable \`myVar\` to **333**
- When a main file sets \`myVar = 89;\` and then requires this module, \`myVar\` ends up as 333
- This task is about **scope** and how requiring a file can modify outer variables

### 15. Call me Moby — \`101-call_me_moby.js\`

- Exports a function \`callMeMoby(x, theFunction)\`
- Calls \`theFunction()\` exactly \`x\` times
- Used like:
  - \`callMeMoby(3, () => console.log('C is fun'))\`

### 16. Add me maybe — \`102-add_me_maybe.js\`

- Exports a function \`addMeMaybe(number, theFunction)\`
- Increments \`number\` by 1, then calls \`theFunction\` with the new value
- Example: prints \`New value: 5\` when called with 4

### 17. Increment object — \`103-object_fct.js\`

- Starts with an object that has a \`value\` property set to 12
- Adds a new method \`incr\` to the object
- Each time \`myObject.incr()\` is called, \`value\` increases by 1
- The script logs the object multiple times to show the value going from 12 → 13 → 14 → 15

---

This project is a quick tour through:
- basic printing,
- arguments with \`process.argv\`,
- loops and conditionals,
- recursion,
- object mutation,
- and exporting functions so they can be reused in other files.
