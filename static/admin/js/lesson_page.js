window.addEventListener('beforeunload', function (e) {
  if (document.querySelector(".markdownx > textarea").value.trim() == '') return;
  // Cancel the event
  e.preventDefault(); // If you prevent default behavior in Mozilla Firefox prompt will always be shown
  // Chrome requires returnValue to be set
  e.returnValue = '';
});

// document.querySelector(".markdownx > .markdownx-preview").classList.add("lesson-page");

window.addEventListener('load', function () {
  document.querySelector(".markdownx > .markdownx-preview").id = ("lesson-preview");
});