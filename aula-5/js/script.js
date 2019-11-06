let login = "jhonny";
let senha = "123";
let x;
let y;
let i=0;
 



while(i<5){
    x = prompt("digite o login");
    y = prompt("digite a senha");
    if(login ==  x && senha == y){
        alert("bem vindo ao sistema");
        i=5;
    }else{        
        i++;
        alert("senha ou usuario errado tentativa "+ i);
    }
}