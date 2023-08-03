// fetch('https://fakestoreapi.com/products')
// .then((data) => {
//     // console.log(data);
//     return data.json();
// })
// .then((apidata)=>{
//     // console.log(apidata);
//     let data1="";
//     apidata.slice(0,4).map((values)=>{
//         data1+=`<div class="col-3 product-card">
//                     <div class="card-item">
//                         <div class="product-wrapper">
//                             <img class="card-img" src=${values.image} alt="img">
//                             <div class="ofr-price">${values.price}$</div>
//                             <div class="product-cat">${values.category}</div>
//                             <a href="#" class="card-title">${values.title}</a>
//                         </div>
//                     </div>
//                 </div>` ;
//     });
//     document.getElementById("cards").innerHTML = `<div class="row">${data1}</div>`;
    
// }).catch((error)=>{
//     console.log(error);
// })



 // Add click event listener to the "Dashboard" menu item
//    document.querySelector('.dashboard-menu li.nav-item:nth-child(1) a').addEventListener('click', function(event) {
//        event.preventDefault(); // Prevent default link behavior
//        document.getElementById('dashboardDetail').style.display = 'block'; // Set display to block for "Edit Profile" content
//        document.getElementById('editProfileContent').style.display = 'none';
//        document.getElementById('orderContent').style.display = 'none';
//        document.getElementById('addressContent').style.display = 'none';
//    });
//
//    document.querySelector('.dashboard-menu li.nav-item:nth-child(2) a').addEventListener('click', function(event) {
//        event.preventDefault(); // Prevent default link behavior
//        document.getElementById('editProfileContent').style.display = 'block';
//        document.getElementById('addressContent').style.display = 'none';
//        document.getElementById('dashboardDetail').style.display = 'none';
//        document.getElementById('orderContent').style.display = 'none'; // Set display to none for "Edit Profile" content
//    });
//    document.querySelector('.dashboard-menu li.nav-item:nth-child(3) a').addEventListener('click', function(event) {
//        event.preventDefault(); // Prevent default link behavior
//        document.getElementById('orderContent').style.display = 'block';
//        document.getElementById('addressContent').style.display = 'none';
//        document.getElementById('editProfileContent').style.display = 'none';
//        document.getElementById('dashboardDetail').style.display = 'none';// Set display to none for "Edit Profile" content
//    });
//    document.querySelector('.dashboard-menu li.nav-item:nth-child(5) a').addEventListener('click', function(event) {
//        event.preventDefault(); // Prevent default link behavior
//        document.getElementById('addressContent').style.display = 'block';
//        document.getElementById('orderContent').style.display = 'none';
//        document.getElementById('editProfileContent').style.display = 'none';
//        document.getElementById('dashboardDetail').style.display = 'none';// Set display to none for "Edit Profile" content
//    });




    //popup
//    function popupFunction(){
//        document.getElementById("popupForm").style.display="block";
//        return false;
//    }
//    function closePopupForm(){
//        document.getElementById("popupForm").style.display="none";
//    }

    //address
//    function addpopupFunction(){
//        document.getElementById("addpopupForm").style.display="block";
//        return false;
//    }
//    function closePopupFunction(){
//        document.getElementById("addpopupForm").style.display="none";
//
//    }

    //change password popup
    function popupPassword(){
        document.getElementById("passwordId").style.display="block";
        return false;
    }
    function closePopup(){
        document.getElementById("passwordId").style.display="none";
       
    }