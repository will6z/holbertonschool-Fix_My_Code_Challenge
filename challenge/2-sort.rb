###
#
#  Sort numeric arguments (ascending) 
#
###

result = []
ARGV.each do |arg|
    # skip if not numeric
    next if arg !~ /^-?[0-9]+(\.[0-9]+)?$/

    # convert to float
    f_arg = arg.to_f
    
    # insert result at the right position
    is_inserted = false
    i = 0
    l = result.size
    while !is_inserted && i < l do
        if result[i] > f_arg
            result.insert(i, f_arg)
            is_inserted = true
            break
        end
        i += 1
    end
    result << f_arg if !is_inserted
end

puts result
