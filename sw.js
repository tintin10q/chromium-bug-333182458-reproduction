


addEventListener("push", event => {
    console.log("Got push event", event)
    console.info("Got data from push event", event.data)
    event.waitUntil(handle_push(event))
})

async function handle_push(event) {
    let data = event.data;
    if (data === null) return self.registration.showNotification("Data is null!!");

    const data_blob = await event.data.blob();
    const data_stream = data_blob.stream()
    const response = new Response(data_stream)
    const stream_data = await response.arrayBuffer() 
    const length = stream_data.byteLength;
    return self.registration.showNotification(`Received ${length} bytes in push event.`);
}

addEventListener("install", event => {
    self.skipWaiting()
    console.log("Installing service worker")
})

addEventListener("activate", event => {
    console.log("Activated service worker")
})