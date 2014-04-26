
(*
 * Highly optimized code,
 * breaks a few best practices
 * for the sake of speed
*)

let explode str =
    let len = String.length str in
    let rec aux counter lst =
        if counter < 0 then (lst, len) else aux (counter - 1) ((String.get str counter) :: lst)
    in aux (len - 1) []
;;

let load_cases t =
    let rec aux t cases =
        match t with
        | 1 -> 
            let patient = read_line () in
            let virus = read_line () in
            ((patient, virus)::cases)
        | t ->
            let patient = read_line () in
            let virus = read_line () in
            let _ = read_line () in
            aux (t - 1) ((patient, virus)::cases)
    in aux t []
;;

let find_matches patient virus =
    let p, p_len = (explode patient) in
    let v, v_len = (explode virus) in
    let rec check_match patient virus mismatch =
        match patient, virus with
        | p_hd::p_tl, v_hd::v_tl when p_hd != v_hd -> mismatch && check_match p_tl v_tl false
        | p_hd::p_tl, v_hd::v_tl -> check_match p_tl v_tl mismatch
        | _, [] -> true
        | [], _ -> false
    in
    let rec aux patient p_len counter = 
        if p_len < v_len then ()
        else
            (
                (
                    if check_match patient v true
                    then ( print_int counter; print_char ' '; )
                );
                aux (List.tl patient) (p_len - 1) (counter + 1) 
            )
    in aux p p_len 0
;;

let exec_case (patient, virus) =
    find_matches patient virus;
    print_newline()
;;
 
let rec exec_cases = function
    | case::cases ->
            exec_case case;
            exec_cases cases
    | [] -> ()
;;

let () =
    let t = read_int() in
    let cases = List.rev (load_cases t) in
    exec_cases cases
;;

