const firstname = document.getElementById("firstname");
const middlename = document.getElementById("middlename");
const lastname = document.getElementById("lastname");
const regNo = document.getElementById("regNo");
const email = document.getElementById("emailNo");
const phoneNo = document.getElementById("phoneNo")
const btn = document.getElementById("btn");
const container2 = document.querySelector(".container2");
const container3 = document.querySelector(".container3");
const table = document.getElementById("table-body");
const users = [];
let count = 1;
function send(){
    // container2.style.display = "block";
    container3.style.display = "block";
    
    users.push({
        count: count,
        firstname: firstname.value,
        middlename: middlename.value,
        lastname: lastname.value,
        email: email.value,
        regNo: regNo.value,
        phoneNo: phoneNo.value
    })
    console.log(users)
    
    users.forEach(function (user) {
        const tr = `
        <tr id = ${count}>
            <td>${count}</td>
            <td>${user.firstname}</td>
            <td>${user.middlename}</td>
            <td>${user.lastname}</td>
            <td>${user.email}</td>
            <td>${user.regNo}</td>
            <td>${user.phoneNo}</td>
        </tr>
        `;
        table.insertAdjacentHTML("beforebegin", tr);
    });
    count++;
}
const rUsers = users
localStorage.setItem('ruser', JSON.stringify(rUsers));
const usersData = JSON.parse(localStorage.getItem('ruser'));