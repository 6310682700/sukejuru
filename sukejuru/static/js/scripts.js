/*!
* Start Bootstrap - Shop Homepage v5.0.5 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


const one = document.getElementById("first")
const two = document.getElementById("second")
const three = document.getElementById("third")
const four = document.getElementById("fourth")
const five = document.getElementById("fifth")
const load = document.getElementById("load")

const form = document.querySelector('.rate-form')
const confirmBox = document.getElementById('confirm-box')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

$(document).ready(function() {
    handleStarSelect(load.value);
    console.log(load.value)
    
});

// function Loadpage() {
//     handleStarSelect(load.value);
//     console.log("Hello")
// }
// window.onload = 

const handleStarSelect = (size) => {
    const children = form.children
    for (let i=0; i < children.length; i++) {
        if(i <= size) {
            children[i].classList.add('checked')
        } else {
            children[i].classList.remove('checked')
        }
    }
}

console.log(one)

const handleSelect = (selection) => {
    switch(selection) {
        case "first": {
            handleStarSelect(1)
            return
        }
        case "second": {
            handleStarSelect(2)
            return
        }
        case "third": {
            handleStarSelect(3)
            return
        }
        case "fourth": {
            handleStarSelect(4)
            return
        }
        case "fifth": {
            handleStarSelect(5)
            return
        }

    }
}

const getNumericValue = (stringValue) => {
    let numericValue;
    if (stringValue === 'first') {
        numericValue = 1
    }
    else if (stringValue === 'second') {
        numericValue = 2
    }
    else if (stringValue === 'third') {
        numericValue = 3
    }
    else if (stringValue === 'fourth') {
        numericValue = 4
    }
    else if (stringValue === 'fifth') {
        numericValue = 5
    }
    else {
        numericValue = 0
    }
    return numericValue
    
}

if(one) {
    const arr = [one, two, three, four, five]

    arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
        handleSelect(event.target.id)
    }))

    arr.forEach(item=> item.addEventListener('click', (event)=>{
        const val = event.target.id
        console.log(val)

        let isSubmit = false
        form.addEventListener('submit', e=>{
            e.preventDefault()
            if (isSubmit) {
                return
            }
            isSubmit = true
            const id = e.target.id
            console.log(id)
            const val_num = getNumericValue(val)

            $.ajax({
                type: 'POST',
                url: '/rate',
                data: {
                    'csrfmiddlewaretoken': csrf[0].value,
                    'el_id': id,
                    'val': val_num,
                },
                success: function(response){
                    console.log(response)
                    confirmBox.innerHTML = `<h5>Successfully rated with ${response.score}</h5>`
                },
                error: function(error){
                    console.log(error)
                    confirmBox.innerHTML = `<h5...Something went wrong</h5>`
                }
            })
        })
    }))
}