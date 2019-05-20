drop function if exists shorten;
delimiter ;;
create function shorten(s varchar(255), n int) returns varchar(255)
begin
	if isnull(s) then
		return '';
	elseif n<15 then
		return left(s,n);
	else
		if char_length(s)<=n then
			return s;
		else
			return concat(left(s,n-10), '...', right(s,5));
		end if;
	end if;
end;;
 
