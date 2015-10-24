# 試行錯誤的なものに便利な環境の例

## 全部実行したい場合

```bash
$ make clean
rm -rf source normalized summary
$ make default
python -m misc.cli.nums --items=10 --nums=10 --outfile=source/
..........mkdir -p normalizeed
python -m misc.cli.abs --outfile=normalizeed/ source/
..........mkdir -p summary
python -m misc.cli.summary --outfile=summary/ normalizeed/
..........echo ok
ok
```

## 1ステップずつ実行したい場合

```bash
$ make one
mkdir -p source
python -m misc.cli.nums --items=10 --nums=10 --outfile=source/
..........$ make two
mkdir -p normalizeed
python -m misc.cli.abs --outfile=normalizeed/ source/
..........$ make three
mkdir -p summary
python -m misc.cli.summary --outfile=summary/ normalizeed/
..........$ 
```

## 特定のfileだけ実行したい場合

```bash
$ TARGET=001.json make default
mkdir -p source
python -m misc.cli.nums --items=10 --nums=10 --outfile=source/
..........mkdir -p normalizeed
python -m misc.cli.abs --outfile=normalizeed/001.json source/001.json
.mkdir -p summary
python -m misc.cli.summary --outfile=summary/001.json normalizeed/001.json
.(test -f summary/001.json && cat summary/001.json) || echo ok
{
  "src": "001.json",
  "sum": 5.312648568992502,
  "mean": 0.5312648568992503,
  "median": 0.573514029907352,
  "sd": 0.2982669362736558
}
```

## 直接１つのファイルに対して実行した結果が見たい場合

```bash
$ python -m misc.cli.summary normalizeed/007.json 
{
  "src": "007.json",
  "sum": 3.5159586267734997,
  "mean": 0.35159586267735,
  "median": 0.28864790323731593,
  "sd": 0.2682584931875431
}.
```

## 結果を１つのファイルにまとめたい場合

```bash
$ python -m misc.cli.summary normalizeed/ --outfile=./concatnated.json
```