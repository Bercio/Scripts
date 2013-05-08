#
#Look up weather there is an alias for the argument given.
#
# Author:
#   Lorenzo Bercelli <https://github.com/bercio>
#
local usage flag lookup
usage="$(
cat <<EOF
usage: $0 [-option ...] [--] command 

options:
  -e    find only the alias that matches exactly the command given
EOF
)"

while getopts ':e' opt; do
  case "$opt" in                   
      (e) flag="true";;
      ([?])
        print "$0: unknown option: $OPTARG" &&
        print "$usage" &&
        return 1
      ;;
  esac
done
shift $(( $OPTIND - 1 ))
print $@
if (( $# < 2 )); then
  print "$usage" &&
  return 1
fi
if [[ -n $flag ]]; then
    lookup=$(alias | grep -E "^.+='?$@'?$");
else
    lookup=$(alias | grep -E "^.+='?$@.*'?$");
fi
[[ -n $lookup ]]&& 
print "There are some aliases: $lookup"
&& return 0
