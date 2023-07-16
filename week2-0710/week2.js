// Task 1 )
console.log("-----Task1-----");

function findAndPrint(messages) {
  const olderThan17 = [];

  for (const name in messages) {
    const message = messages[name];

    if (
      message.includes("18 years old") ||
      message.includes("college student") ||
      message.includes("legal age") ||
      message.includes("vote")
    ) {
      olderThan17.push(name);
    }
  }

  console.log(olderThan17);
}

findAndPrint({
  Bob: "My name is Bob. I'm 18 years old.",
  Mary: "Hello, glad to meet you.",
  Copper: "I'm a college student. Nice to meet you.",
  Leslie: "I am of legal age in Taiwan.",
  Vivian: "I will vote for Donald Trump next week",
  Jenny: "Good morning.",
});

// Task 2)
console.log("-----Task2-----");
// bonus rules :   The bonus is calculated as Salary * Performance * Role.
// 1.performance : a) Above average * 0.3
//                 b) AbortControllerverage * 0.2
//                 c) Below average * 0.1

// 2.role        : a) Engineer and Sales * 0.2
//                 b) CEO * 0.5

function calculateSumOfBonus(data) {
  let bonusSum = 0;

  data.employees.forEach(function (employee) {
    let salary = employee.salary;

    if (typeof salary === "string" && salary.includes("USD")) {
      salary = parseInt(salary.replace("USD", "")) * 30;
    } else if (typeof salary === "string") {
      salary = parseInt(salary.replace(",", ""));
    }

    let performance = employee.performance;
    let role = employee.role;

    let bonus = 0;
    if (performance === "above average") {
      bonus = salary * 0.3;
    } else if (performance === "average") {
      bonus = salary * 0.2;
    } else if (performance === "below average") {
      bonus = salary * 0.1;
    }

    if (role === "Engineer" || role === "Sales") {
      bonus *= 0.2;
    } else if (role === "CEO") {
      bonus *= 0.5;
    }

    bonusSum += bonus;
  });

  console.log(`Sum of Bonus : ${bonusSum} NTD`);
}

calculateSumOfBonus({
  employees: [
    {
      name: "John",
      salary: "1000USD",
      performance: "above average",
      role: "Engineer",
    },
    {
      name: "Bob",
      salary: 60000,
      performance: "average",
      role: "CEO",
    },
    {
      name: "Jenny",
      salary: "50,000",
      performance: "below average",
      role: "Sales",
    },
  ],
});

// Task 3)
console.log("-----Task3-----");

function func(...data) {
  const middleNameCounts = {};
  let uniqueMiddleName = "";

  for (let i = 0; i < data.length; i++) {
    const name = data[i];
    const nameArray = name.split("");

    const middleNameIndex = Math.floor(nameArray.length / 2);
    const middleName = nameArray[middleNameIndex];

    if (middleNameCounts[middleName] === undefined) {
      middleNameCounts[middleName] = 1;
    } else {
      middleNameCounts[middleName]++;
    }
  }

  for (let i = 0; i < data.length; i++) {
    const name = data[i];
    const nameArray = name.split("");

    const middleNameIndex = Math.floor(nameArray.length / 2);
    const middleName = nameArray[middleNameIndex];

    if (middleNameCounts[middleName] === 1) {
      uniqueMiddleName = name;
      break;
    }
  }

  if (uniqueMiddleName !== "") {
    console.log(uniqueMiddleName);
  } else {
    console.log("沒有");
  }
}

func("彭大牆", "王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有

// Task 4)
console.log("-----Task4-----");

function getNumber(index) {
  if (index <= 0) {
    return 0;
  }

  let number = 0;

  for (let i = 1; i <= index; i++) {
    if (i % 2 === 1) {
      number += 4;
    } else {
      number -= 1;
    }
  }

  return number;
}

console.log(getNumber(1)); // 印出 4
console.log(getNumber(5)); // 印出 10
console.log(getNumber(10)); // 印出 15

// Task 5)
console.log("-----Task5-----");

function findIndexOfCar(seats, status, x) {
  let answer = -1;
  for (let i = 0; i < seats.length; i++) {
    if (status[i] == 1 && seats[i] >= x) {
      if (answer == -1) {
        answer = i;
      } else if (seats[i] < seats[answer]) {
        answer = i;
      }
    }
  }
  return answer;
}

console.log(findIndexOfCar([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2)); // print 4
console.log(findIndexOfCar([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4)); // print -1
console.log(findIndexOfCar([4, 6, 5, 8], [0, 1, 1, 1], 4)); // print 2
