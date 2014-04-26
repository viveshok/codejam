
let load_cases t =
    let rec aux t cases =
        match t with
        | 1 ->
            let case = (read_line (), read_line ()) in
            (case::cases)
        | t ->
            let case = (read_line (), read_line ()) in
            let _ = read_line () in
            aux (t - 1) (case::cases)
    in aux t []
;;

let exec_case = function
    | input, output -> print_string ("input: "^input^", output: "^output^"\n")
;;
 
let rec exec_cases = function
    | case::cases ->
            exec_case case;
            exec_cases cases
    | [] -> ()
;;

let () =
    let t = int_of_string(read_line ()) in
    let cases = load_cases t in
    exec_cases cases
;;

