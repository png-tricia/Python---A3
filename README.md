## PROG12583 Programming Foundations - Python: Assignment 3
Program: **Computer Programming @ Sheridan College** <br>
Note: The following assignment was completed during Semester 1 (2023) <br>

## The Task:
Create a program that calculates the employees wages. 

## The Details:
**Requirements**:
<ul>
  <li>DO NOT USE while true, break or continue</li>
  <li>the program should contain a global dictionary that contains:<br> 101:'Fred Budd', 103:'Barney Stone', 106:'Wilma Flint',  109:'Betty Rubble', 112:'Dino Dawg' </li>
  <li>the program should contain a minimum of four functions:
    <ul>
      <li>checkID
        <ul>
          <li>takes a parameter called id </li>
          <li>searches the id of the dictionary </li>
          <li>returns True if the id is in the dictionary </li>
          <li>returns False otherwise </li>
        </ul>
      </li>
      <li>findName
        <ul>
          <li>takes an id parameter</li>
          <li>searches the dictionary for the name associated with the id</li>
          <li>returns the name or “Not Found”</li>
        </ul>
      </li>
      <li>calculatePay
        <ul>
          <li>takes two parameters: hours worked and hourly rate</li>
          <li>if hours exceed 40 then any overtime hours are paid time and a half ➡️ if 45 hours, then 5 hours paid at 1.5 * rate</li>
          <li>weekly pay = hours worked * hourly rate + overtime pay</li>
          <li>returns weekly pay</li>
        </ul>
      </li>
      <li>calculateTax
        <ul>
          <li>takes a parameter called wage</li>
          <li>uses the table below</li>
          <li>returns the taxes owed</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>

**The Main Class** prompts the user to choose from:<br>
<ol>
  <li>Add Worker</li> 
  <li>Process Worker </li> 
  <li>Display All Workers ID and Name </li> 
  <li>Display Processed Workers </li> 
  <li>End Program </li>
</ol>

## Thoughts/Comments: 
Main takeaway - dictionaries and lists, functions, formatting 
