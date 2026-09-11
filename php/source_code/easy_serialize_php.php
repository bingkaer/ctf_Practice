<?php

$function = @$_GET["f"];

// 过滤
function filter($img)
{
    $filter_arr = ["php", "flag", "php5", "php4", "fl1g"];
    $filter = "/" . implode("|", $filter_arr) . "/i";
    return preg_replace($filter, "", $img);
}

//重置（清空）当前的会话（Session）数据，然后初始化一个新的会话状态
if ($_SESSION) {
    unset($_SESSION);
}

$_SESSION["user"] = "guest";
$_SESSION["function"] = $function;

//引入post,可以替换上面的$_SESSION
extract($_POST);

//初始查看源码
if (!$function) {
    echo '<a href="index.php?f=highlight_file">source_code</a>';
}

// 图片路径不存在逻辑
if (!$_GET["img_path"]) {
    $_SESSION["img"] = base64_encode("guest_img.png");
} else {
    //无法控制img
    $_SESSION["img"] = sha1(base64_encode($_GET["img_path"]));
}

//先序列化再过滤
// 固定至少3个元素user function img
$serialize_info = filter(serialize($_SESSION));

if ($function == "highlight_file") {
    //默认 获取源码
    highlight_file("index.php");
} elseif ($function == "phpinfo") {
    // 查看 php信息
    eval("phpinfo();"); //maybe you can find something in here!
} elseif ($function == "show_image") {
    //反序列入口
    $userinfo = unserialize($serialize_info);
    echo file_get_contents(base64_decode($userinfo["img"]));
}
