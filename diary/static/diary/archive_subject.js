const buttons = document.querySelectorAll(`.btn_fin`)

for (let btn of buttons){
    btn.addEventListener(`click`, async ()=>{
        console.log(btn.id)
        const url = "/subject/archive/";
        try {
            const response = await fetch(url, {
                method: "POST",
                body: JSON.stringify({ 'id': `${btn.id}`}),
            });
            if (!response.ok) {
                console.log(await response.json());
                throw new Error(`Response status: ${response.status}`);
            }

            const item = document.querySelector(`#li_${btn.id}`) 
            item.remove()
            }
      catch (error) {
            console.error(error.message);
      }

    })
}
