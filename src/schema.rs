table! {
    hosts (id) {
        id -> Uuid,
        name -> Varchar,
        address -> Varchar,
        port -> Int4,
        status -> Varchar,
        host_user -> Varchar,
        password -> Varchar,
    }
}

table! {
    vms (id) {
        id -> Uuid,
        name -> Varchar,
        status -> Int4,
        host_id -> Nullable<Uuid>,
        vcpu -> Int4,
        memory -> Int4,
        kernel -> Varchar,
        root_file_system -> Varchar,
    }
}

joinable!(vms -> hosts (host_id));

allow_tables_to_appear_in_same_query!(
    hosts,
    vms,
);
