import './styles.scss';

const messageError = document.querySelector(".message");
const messageText = document.querySelector(".message__text");
const closeMessage = document.querySelector(".close");
const spinnerLoader = document.querySelector("#spinner");
const modalLoader = document.querySelector(".modal");

const mainWrapper = document.querySelector(".main-wrapper");
const slideContainer = document.querySelector(".slideshow-container");
const exitBtn = document.querySelector(".remove-button");
let newImageDrop;



exitBtn.addEventListener("click", exitSlider);
// closeMessage.addEventListener("click", closeAlert);

// message error if the button ok is pressed the box disappear
// function closeAlert () {
//   messageError.style.display = "none";
// }

const inputImage = document.querySelector("#images-upload");
const modalGallery = document.querySelector(".load-images-gallery__modal");
const imageSelected = document.querySelector(".load-images-gallery__container");
const loadImageSquare = document.querySelector(".load-images-gallery__upload");
const submitResultsList = document.querySelector(".load-images-gallery__submit");

let newImage;
let errorFormat;

submitResultsList.addEventListener("click", function(e){
      // e.preventDefault();
      fetch(window.location).then(function (response) {
        return response.json();
        console.log(response.json())
      }).then(function (data) {
        console.log(data);
      })  
});

(function init() {
    inputImage.addEventListener("change", selectImage);
})();

['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
  loadImageSquare.addEventListener(eventName, preventDefaults, false)
})

function preventDefaults (e) {
  e.preventDefault()
  e.stopPropagation()
}


loadImageSquare.addEventListener('drop', handleDrop, false)

function handleDrop(e) {
let dt = e.dataTransfer
let files = dt.files

handleFiles(files)
}

function previewFile(file) {
  let reader = new FileReader()
  reader.readAsDataURL(file)
  reader.onloadend = function() {
   loadImage(this.result);
  }
}

function handleFiles(files) {
  files = [...files]
  files.forEach(previewFile)
}



function selectImage() {
    if(errorFormat !== undefined) {
        errorFormat.innerText = "";
    }
    const image = this.files[0];
    if(image.type == "image/jpeg" || image.type == "image/png") {
        const reader = new FileReader();
        reader.addEventListener("load", loadImage);
        reader.readAsDataURL(image);
    } else {
        errorFormat = document.createElement("p");
        errorFormat.innerText = "The format of the file is invalid";
        loadImageSquare.appendChild(errorFormat);
    }

}
        
function loadImage(src) {
    const imageBox = document.createElement("div");
    const removeBtn = document.createElement("p");

    imageBox.classList.add("imageSelected");
    removeBtn.classList.add("removeImage");
    removeBtn.innerHTML = "X"
    newImage = new Image();
    newImageDrop = new Image();
    newImage.classList.add("readyImage");
    newImageDrop.classList.add("readyImage");
    newImage.style.maxWidth = "100%";
    newImageDrop.style.maxWidth = "100%";
    newImage.style.maxHeight = "400px";
    newImageDrop.style.maxHeight = "400px";

    if(this.result == undefined) {
        newImageDrop.src = src;
    } else {
        newImage.src = this.result;
    };
    imageBox.appendChild(newImage);
    imageBox.appendChild(newImageDrop);
    imageBox.appendChild(removeBtn);
    loadImageSquare.appendChild(imageBox);

    Array.from(loadImageSquare.children).forEach(function(element) {
        element.querySelector(".removeImage").addEventListener("click", function(e) {
            e.preventDefault();
            if(loadImageSquare.children.length >= 1 ) {
                element.remove();
            }
            
        });
    });

//     console.log(newImage);
// let imagePath = newImage.src;

        
//         Array.from(loadImageSquare.children).forEach(function(element,i) {
//             createSlide(imagePath,i );
//         })
//         upload.addEventListener("click", createSlide);
        
//         function createSlide(path, index){
          
//             const slides = document.createElement("div");
//     slides.classList.add("slides-image-container");
//     if(index == 0) {
//       slides.style.display = "block";
//     } 
//     const image = new Image();
//     const result = document.createElement("div");
//     result.classList.add("result-wrapper");

//     image.classList.add("image");
//     image.src = path;

//     slides.appendChild(image);
//     slides.appendChild(result);
//     slides.children[0].style.display = "block";
//     slideContainer.appendChild(slides);
//   }
}

/*DROPZONE CUSTOMIZE CONFIGURATION
Dropzone.options.myawesomedropzone = {
  init: function() {
    
      this.on('addedfile', function(file) {
        // if the files are more than 10 an error message appear and the 10^ element will be removed
          if(this.files.length > 10) {
              this.removeFile(this.files[10]);
              messageError.style.display = "inline-block";
              messageText.innerHTML = "no more than 10";
          } else {
              messageError.style.display = "none";
          }
       });
       this.on('removedfile', function(file) {
         // if the button remove file (under the image) is pressed and the files are less than 10, the box error disappear
          if(this.files.length < 10) {
              messageError.style.display = "none";
          } else {
              messageError.style.display = "inline-block";
          }
       });
       /* "this" is a reference to myDropzone. I add to call it outside the button funtion below because otherwise
       it gives me a different value linked with the button
       
       let myDropzone = this;
       document.querySelector("#button").addEventListener("click", function (e){
         //spinnerLoader.style.visibility = "visible";
         e.preventDefault();
         myDropzone.processQueue();    
         //modalLoader.style.display ="block";
         e.preventDefault();
         myDropzone.processQueue(); 
         /* if there are more than 0 slides already in the slider (maybe because i uploaded images before)
        it will remove them
         if(document.querySelectorAll(".slides-image-container").length > 0) {
            document.querySelectorAll(".slides-image-container").forEach(function(element) {
              element.parentNode.removeChild(element);
         })};
         /* here i take the files property of the object mydropzone and a pass the dataURL that is a reference to the image.
          i need that because the tag img needed it in the src
          myDropzone.files.forEach(function(element,i) {
            createSlide(element.dataURL, i)
          });
          // here I removed all the files from the dropzone when upload is clicked
          //myDropzone.removeAllFiles();
          mainWrapper.style.display = "block";

         // document.querySelector(".slides-image-container").innerHTML = "";
         
        
         /* e.preventDefault();
          myDropzone.processQueue();    
          
        });
      },
}
*/
/* Here I create the slides that composed the slideshow, i assigned the dataURL to the src,
based on the slider built by Manuel I give to the first slide the display block (index 0)
function createSlide(imageSrc, index) {
    const slides = document.createElement("div");
    slides.classList.add("slides-image-container");
    if(index == 0) {
      slides.style.display = "block";
    } 
    const image = new Image();
    const result = document.createElement("div");
    result.classList.add("result-wrapper");

    image.classList.add("image");
    image.src = imageSrc;

    slides.appendChild(image);
    slides.appendChild(result);
    slides.children[0].style.display = "block";
    slideContainer.appendChild(slides);
}
*/
// button to exit from the slider when the modal appear
function exitSlider () {
  mainWrapper.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == mainWrapper) {
    mainWrapper.style.display = "none";
  }
}

/* Default slide index is 1 */
var slideIndex = 1;
var slides = document.getElementsByClassName("slides-image-container");
showSlides(slideIndex);
const prevButton = document.querySelector(".prev");
const nextButton = document.querySelector(".next");

/* Callback for previous button */
prevButton.addEventListener("click", function(){
  plusSlides(-1);
});

/* Callback for next button */
nextButton.addEventListener("click", function(){
  plusSlides(1);
});

/* Next / previous controls */
function plusSlides(n) {
  console.log("Slider buttons are working correctly");

  /* Increase slide index when you press the button next and decrease it when you press the button previous */
  showSlides(slideIndex += n);
}

/* Thumbnail image controls 
 function currentSlide(n) {
   showSlides(slideIndex = n);
}*/

function showSlides(n) {
  var arr = Array.from(slides);
      console.log(arr);
 console.log(slides);
    var i;

  
    if(slides.length >0) {
      
      if (n > slides.length) {slideIndex = 1}
  
      if (n < 1) {slideIndex = slides.length}
    
      /* Display none applied to the slide if it is not the one displayed on the screen*/
    
      for (i = 0; i < slides.length; i++) {
          slides[i].style.display = "none";
      }
    
      /* Display the slide using display block if it is the one we're seeing on the screen */
      console.log(slides);
      slides[slideIndex-1].style.display = "block";
    }
  
  }

  





