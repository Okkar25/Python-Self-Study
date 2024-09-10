class Person {
  constructor(name, age, job, salary) {
    this.name = name;
    this.age = age;
    this.job = job;
    this.#salary = salary;
  }

  #salary;

  getSalary() {
    return this.#salary;
  }

  static gender = "male";

  static getGender() {
    return this.gender;
  }

  // private value
  #subjects = {
    majorSubs: ["DSA", "Frontend", "Database", "Programming"],
    minorSubs: ["English Literature", "US History", "Business"],
  };

  // encapsulation
  getMajor() {
    return `My favorite major sub is ${
      this.#subjects["majorSubs"][3]
    } and minor is ${this.#subjects["minorSubs"][2]}`;
  }

  // getter
  getJob() {
    return this.job;
  }

  // setter
  setJob(newJob) {
    return (this.job = newJob);
  }
}

const person1 = new Person(
  "Okkar",
  23,
  "Software Developer",
  "Computer Science"
);
// console.log(person1.getJob());
// console.log(person1.setJob("Web Developer"));
// console.log(person1.gender);
// console.log(Person.gender);
// console.log(Person.getGender());
// console.log(person1.#subjects["majorSubs"][2]); // cannot be called private values directly
// console.log(Person.#subjects["majorSubs"][2]);
// console.log(person1.getMajor());
// console.log(Person.getMajor());

// inheritance

class Car {
  constructor(brand, color) {
    this.brand = brand;
    this.color = color;
  }

  getColor() {
    return this.color;
  }
}

// const car1 = new Car("Super Salon", "white", 2003);
// console.log(car1);

class Toyota extends Car {
  constructor(brand, color, releaseDate) {
    super(brand, color); // inherit Car constructor
    this.releaseDate = releaseDate;
  }

  getColor() {
    return `this is ${this.brand} overwrite parent Car values - ${this.color}`;
  }

  getReleaseDate() {
    return this.releaseDate;
  }
}

const toyota = new Toyota("Toyota", "black", 1998);
// console.log(toyota.getColor());

class Swift extends Toyota {
  constructor(brand, color, releaseDate, company) {
    super(brand, color, releaseDate);
    this.company = company;
  }

  getReleaseDate() {
    return `This is overwriting parent Toyota class value - ${this.company}`;
  }

  getColor() {
    return "Overwriting grandfather class value " + this.company;
  }
}

const swift = new Swift("Swift", "red", 2008, "InnoTech");
// console.log(swift.getColor());
// console.log(swift.getColor());

// ------------------------------------------------------------------------------------------------------------------------

//  constructor function

function Laptop(brand, color) {
  this.brand = brand;
  this.color = color;
}

Laptop.prototype.getBrand = function () {
  return this.brand;
};

const laptop = new Laptop("Dell", "Space Grey");
// console.log(laptop.getBrand());

function Lenovo(brand, color, price) {
  Laptop.call(this, brand, color);
  this.price = price;
}

Lenovo.prototype = Object.create(Laptop.prototype);

const lenovo = new Lenovo("Lenovo", "black", "$700");
// console.log(lenovo.getBrand());

// ------------------------------------------------------------------------------------------------------------------------

const carPrototype = {
  getSpeed: function () {
    return this.speed;
  },
  getName: function () {
    return this.name;
  },
};

const car1 = Object.create(carPrototype);
car1.speed = 2200;
car1.name = "Honda";

// console.log(car1);
// console.log(car1.getSpeed());

const car2 = Object.create(carPrototype, {
  name: { value: "Swift" },
  speed: { value: 3000 },
});

// console.log(car2.getName());
// console.log(car2.speed);
