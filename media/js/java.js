function Real_fixPNG(element)
{
  if (/MSIE (5\.5|6).+Win/.test(navigator.userAgent))
  {
    var src;

    if (element.tagName=='IMG')
    {
      if (/\.png$/.test(element.src))
      {
        src = element.src;
        element.src = "i/p.gif";
      }
    }
    else
    {
      src = element.currentStyle.backgroundImage.match(/url\("(.+\.png)"\)/i);
      if (src)
      {
        src = src[1];
        element.runtimeStyle.backgroundImage="none";
      }
    }
    if (src) element.runtimeStyle.filter = "progid:DXImageTransform.Microsoft.AlphaImageLoader(src='" + src + "',sizingMethod='scale')";
  }
}

function SetContentHeight()
{
    // Растягивает контент
    var document_width = $(document).width();
    var document_height = $(document).height();
    // Берем из CSS высоты FOOTERa и HEADERa
    var header_height = 200;
    var footer_height = 50;
    content_height = document_height - (header_height + footer_height);
    $("#content").css("height", content_height+"px");
}

$(document).ready(function() {
    //SetContentHeight();
});